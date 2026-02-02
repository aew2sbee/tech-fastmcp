from fastmcp import FastMCP

# サーバーのインスタンス化
mcp = FastMCP("QuickStart")

# シンプルな計算ツールを追加してみます
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """2つの数値を足し合わせます。"""
    return a + b

if __name__ == "__main__":
    mcp.run()