
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # Agar matrix empty hai ya usme koi column nahi hai,
        # toh empty list return kar do.
        if not matrix or not matrix[0]:
            return []

        result = []

        # Chaar boundaries define kar rahe hain
        top = 0
        left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1  # Columns ka last index

        # Jab tak boundaries cross nahi hoti, spiral chalta rahega
        while top <= bottom and left <= right:

            # 1. TOP ROW: Left se right jao
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1  # Top row visit ho gayi, ab neeche move karo

            # 2. RIGHT COLUMN: Top se bottom jao
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # Right column visit ho gaya

            # 3. BOTTOM ROW: Right se left jao
            # Check zaroori hai, warna same elements dobara aa sakte hain
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1  # Bottom row visit ho gayi

            # 4. LEFT COLUMN: Bottom se top jao
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # Left column visit ho gaya

        return result
