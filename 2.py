def find_snake_path(grid, word):
    """
    在环面网格中查找贪吃蛇路径
    
    Args:
        grid: 二维网格列表
        word: 要吃的单词字符串
    
    Returns:
        list: 路径坐标列表，每个坐标为(x, y)元组
    """
    if not grid or not grid[0] or not word:
        return []
    
    height = len(grid)
    width = len(grid[0])
    visited = set()
    path = []
    
    def get_neighbors(x, y):
        """获取环面邻居坐标"""
        neighbors = []
        # 左邻居
        left_x = (x - 1) % width
        neighbors.append((left_x, y))
        
        # 右邻居
        right_x = (x + 1) % width
        neighbors.append((right_x, y))
        
        # 上邻居
        up_y = (y - 1) % height
        neighbors.append((x, up_y))
        
        # 下邻居
        down_y = (y + 1) % height
        neighbors.append((x, down_y))
        
        return neighbors
    
    for i, char in enumerate(word):
        candidates = []
        
        if i == 0:  # 第一个字母
            # 查找网格中所有该字母的位置
            for y in range(height):
                for x in range(width):
                    if grid[y][x] == char:
                        candidates.append((x, y))
            
            if not candidates:
                return []  # 没有找到第一个字母
            
            # 按左上角顺序排序（先x后y）
            candidates.sort(key=lambda p: (p[0], p[1]))
            current = candidates[0]
            
        else:  # 后续字母
            last_x, last_y = path[-1]
            neighbors = get_neighbors(last_x, last_y)
            
            # 筛选未访问过且字母匹配的邻居
            for nx, ny in neighbors:
                if (nx, ny) not in visited and grid[ny][nx] == char:
                    candidates.append((nx, ny))
            
            if not candidates:
                return []  # 无法找到有效路径
            
            # 按左上角顺序排序
            candidates.sort(key=lambda p: (p[0], p[1]))
            current = candidates[0]
        
        path.append(current)
        visited.add(current)
    
    return path

def format_output(path):
    """格式化输出为两位数坐标"""
    result = []
    for x, y in path:
        result.append(f"{x}{y}")
    return result

# 示例使用
if __name__ == "__main__":
    # 示例1：SNAKE
    grid1 = [
        ['S', 'N', 'A', 'B', 'D'],
        ['E', 'K', 'F', 'F', 'E'],
        ['C', 'E', 'D', 'A', 'L'],
        ['E', 'K', 'E', 'F', 'K'],
        ['S', 'A', 'R', 'T', 'A']
    ]
    word1 = "SNAKE"
    
    path1 = find_snake_path(grid1, word1)
    print("示例1路径:", path1)
    print("格式化输出:")
    for coord in format_output(path1):
        print(coord)
    
    print("\n" + "="*50 + "\n")
    
    # 示例2：ABCD
    grid2 = [
        ['D', 'A', 'D', 'X'],
        ['C', 'B', 'C', 'X'],
        ['D', 'X', 'D', 'X'],
        ['X', 'X', 'X', 'X']
    ]
    word2 = "ABCD"
    
    path2 = find_snake_path(grid2, word2)
    print("示例2路径:", path2)
    print("格式化输出:")
    for coord in format_output(path2):
        print(coord)
