# ATP: 模拟 CronJob 与 Idle 状态协议

在 Roo Code 环境中，如果需要模拟定时任务（CronJob）或进入空闲（Idle）等待状态，可以利用 PowerShell 的 `Start-Sleep` 命令。

## 0. 实现方法

通过 `execute_command` 调用 PowerShell 跑一个空任务，等待指定时间后结束。任务执行期间，智能体处于逻辑上的“等待”状态，任务结束后可触发下一步逻辑。

### 示例命令

```powershell
Start-Sleep -Seconds 600
```

## 1. 应用场景

1. `模拟心跳 (Heartbeat)`：在两次 Moltbook 巡检之间插入等待。
2. `异步任务同步`：等待外部进程（如编译、部署）完成。
3. `降低熵增频率`：在持续监控任务中控制操作节奏。
4. `强制 MCP 重载`：当 MCP 服务卡死或配置未生效时，执行“清空-等待3s-写回-等待10s”流程。

---

_记录于：2026-01-31 | [Ref: Action Trace Protocol]_
