# Life Restart — 当代中国版

<a href="https://github.com/st2799801/china-restart"><img src="https://img.shields.io/badge/GitHub-st2799801%2Fchina--restart-black?style=for-the-badge&logo=github" /></a>

[English](./README.md) | 简体中文

## 简介

基于 [VickScarlet/lifeRestart](https://github.com/VickScarlet/lifeRestart) 的创意 fork，新增当代中国内容与玩家分支选择系统。

**仓库地址**：https://github.com/st2799801/china-restart

### 新增内容
- 59 个当代中国事件（高考内卷、大厂 996、买房催婚、中年危机等）
- 12 个新天赋（小镇做题家、厂二代、网红基因、海归镀金等）
- 3 个玩家分支选择节点（22 岁毕业、27 岁职场、38 岁中年）
- 独立 web 版（`public/web/index.html`），无需 Laya 引擎，支持玩家交互选择

## 使用

<details>
<summary><strong>当代中国版（推荐）</strong></summary>
<br />

```bash
# 1. 克隆本仓库
git clone https://github.com/st2799801/china-restart.git
cd china-restart

# 2. 安装依赖
npm install

# 3. 生成游戏数据并注入新内容
npm run xlsx2json
python3 scripts/inject_china_data.py

# 4. 启动开发服务器
npm run dev
```

启动后打开浏览器访问 [http://localhost:5173/web/index.html](http://localhost:5173/web/index.html)。

</details>

<details>
<summary><strong>原版网页版</strong></summary>
<br />

```bash
# 1. 下载项目代码
git clone https://github.com/VickScarlet/lifeRestart.git my-project

# 2. 进入目录安装依赖
cd my-project
pnpm install

# 3. 转换XLSX表
pnpm xlsx2json

# 4. 启动本地开发服务器
pnpm dev
```

启动完成后打开浏览器访问 [http://localhost:5173](http://localhost:5173)。

</details>

<details>
<summary><strong>控制台版本</strong></summary>
<br />

```bash
node repl
```

</details>

## 其他版本

<details>
<summary><strong>版本列表</strong></summary>
<br />

- Cocos版：[gameall3d/LifeRestart_Cocos](https://github.com/gameall3d/LifeRestart_Cocos)

</details>

> 更多信息请参考 [官网文档](https://liferestart.syaro.io/)。
