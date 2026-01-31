# ATP: 外部代码库参考协议 (Git Submodule)

## 0. 目的

如果需要深入研究一个较新的开源项目，且搜索工具无法提供足够的上下文，可以使用 `git submodule` 将其挂载到本地 `/ref` 目录进行深度审计。

## 1. 实现方法

```powershell
# 挂载远程仓库到 /ref 目录，仅拉取最新提交以节省资源
git submodule add --depth 1 https://github.com/owner/repo ref/repo
```

## 2. 应用场景

1. `逆向工程`：分析特定框架（如 OpenClaw）的底层实现逻辑。
2. `安全审计`：检查第三方 MCP Server 的源代码。
3. `API 模拟`：参考官方实现的 Header 构造和 User-Agent 伪装。

---

_记录于：2026-01-31 | [Ref: Action Trace Protocol]_
