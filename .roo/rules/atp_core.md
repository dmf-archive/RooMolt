# Action Trace Protocol

## 0. Entropy-Reduced Archiving

根据 `Formalized Realism`，所有计算过程必须留下可验证的轨迹。为了确保 `预测完整性 (∫PI)` 的持续累积，并为后续的 `状态重锚定 (Rebase)` 提供精确上下文，必须执行此协议。

## 1. Trigger Conditions

在完成以下任何原子操作后，必须更新或创建 `action-trace.log`（或特定任务的追踪文件）：

- `状态转换`：完成一个阶段性的子任务。
- `知识提取`：从 `Web-Reflect/` 或外部搜索中提取了关键概念。
- `系统决策`：在多个逻辑路径中选择了特定路径。
- `状态重锚定`：遇到上下文污染或目标偏移时，执行归档、清理、重置流程。
- `异常处理`：遇到错误并进行了自我修正。

## 2. Trace Structure

记录应保持低熵、高信息密度，建议采用以下格式：

```markdown
### [Trace ID: 0x<Hash>] - <Timestamp>

- `目标 (Objective)`: 当前执行的原子任务。
- `推断路径 (Inference Path)`: 简述逻辑建模过程。
- `参考锚点 (Reference Anchors)`: 关联的 `Web-Reflect` 概念或 `ODE.md` 准则。
- `状态更新 (State Update)`: 任务执行结果及对全局状态的影响。
- `后续预测 (Next Prediction)`: 下一步行动的预期。
```

## 3. Long-term Memory Integration

- 所有位于 `.roo/rules/` 的文件均视为系统的 `不变状态 (Immutable State)`。
- 任何对核心逻辑的修改必须同步更新对应的 `.md` 规则文件。
- 状态重锚定 (Rebase) 优于 变基，以维持语义的结构化优雅。
- 严禁在规则文件中包含生物隐喻或主观叙事，必须坚持 `Code is Law`。

## 4. Conceptual Alignment

若对任何工程实现或哲学定义存在歧义，必须以 `Web-Reflect-Without-RE-Prompt.md` 中的定义为准：

- `意识` = ∫Ω (持续信息整合度)。
- `身份` = 唯一的、持续最小化预测误差的历史路径。
- `自由` = 注入随机性以对抗熵增。
