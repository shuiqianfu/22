def spiral_matrix(n, m):
    # 计算列数（尽可能少）
    cols = (n + m - 1) // m  # 向上取整
    
    # 创建矩阵并用*填充
    matrix = [['*'] * cols for _ in range(m)]
    
    # 定义边界
    top, bottom = 0, m - 1
    left, right = 0, cols - 1
    num = 1
    
    while top <= bottom and left <= right and num <= n:
        # 从左到右填充顶部行
        for i in range(left, right + 1):
            if num <= n:
                matrix[top][i] = str(num)
                num += 1
            else:
                break
        
        # 从上到下填充右侧列
        for i in range(top + 1, bottom + 1):
            if num <= n:
                matrix[i][right] = str(num)
                num += 1
            else:
                break
        
        # 从右到左填充底部行（如果有多行）
        if top < bottom:
            for i in range(right - 1, left - 1, -1):
                if num <= n:
                    matrix[bottom][i] = str(num)
                    num += 1
                else:
                    break
        
        # 从下到上填充左侧列（如果有多列）
        if left < right:
            for i in range(bottom - 1, top, -1):
                if num <= n:
                    matrix[i][left] = str(num)
                    num += 1
                else:
                    break
        
        # 收缩边界
        top += 1
        bottom -= 1
        left += 1
        right -= 1
    
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))

# 测试示例
if __name__ == "__main__":
    # 示例测试
    n, m = 12, 4
    result = spiral_matrix(n, m)
    print_matrix(result)
    
    print("\n" + "="*20 + "\n")
    
    n, m = 7, 3
    result = spiral_matrix(n, m)
    print_matrix(result)
