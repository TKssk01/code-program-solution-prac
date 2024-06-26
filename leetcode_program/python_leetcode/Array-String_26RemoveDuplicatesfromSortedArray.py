{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'List' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mclass\u001b[39;00m \u001b[38;5;21;01mSolution\u001b[39;00m:\n\u001b[0;32m      2\u001b[0m     \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mremoveDuplicates\u001b[39m(\u001b[38;5;28mself\u001b[39m, nums: List[\u001b[38;5;28mint\u001b[39m]) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m \u001b[38;5;28mint\u001b[39m:\n\u001b[0;32m      3\u001b[0m         nums_remove \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mset\u001b[39m(nums)\n",
      "Cell \u001b[1;32mIn[1], line 2\u001b[0m, in \u001b[0;36mSolution\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mclass\u001b[39;00m \u001b[38;5;21;01mSolution\u001b[39;00m:\n\u001b[1;32m----> 2\u001b[0m     \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mremoveDuplicates\u001b[39m(\u001b[38;5;28mself\u001b[39m, nums: List[\u001b[38;5;28mint\u001b[39m]) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m \u001b[38;5;28mint\u001b[39m:\n\u001b[0;32m      3\u001b[0m         nums_remove \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mset\u001b[39m(nums)\n\u001b[0;32m      4\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mlen\u001b[39m(nums_remove)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'List' is not defined"
     ]
    }
   ],
   "source": [
    "class Solution:\n",
    "    def removeDuplicates(self, nums: List[int]) -> int:\n",
    "        nums_remove = set(nums)\n",
    "        return len(nums_remove)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "from typing import List\n",
    "\n",
    "class Solution:\n",
    "    def removeDuplicates(self, nums: List[int]) -> int:\n",
    "        nums_remove = list(set(nums))  # 重複を削除したリストを作成\n",
    "        nums_remove.sort()  # 元の順序を保つためにソート\n",
    "        length_unique = len(nums_remove)  # 重複のない要素数を取得\n",
    "        \n",
    "        # 元のリストの長さを保ちながら、重複部分を None で埋める\n",
    "        for i in range(length_unique):\n",
    "            nums[i] = nums_remove[i]\n",
    "        for i in range(length_unique, len(nums)):\n",
    "            nums[i] = None\n",
    "        \n",
    "        return length_unique\n",
    "\n",
    "# リストを定義する例\n",
    "nums = [1, 2, 2, 3, 4, 4, 5]\n",
    "\n",
    "solution = Solution()\n",
    "result = solution.removeDuplicates(nums)\n",
    "\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Length of unique elements: 5\n",
      "Modified list: [1, 2, 3, 4, 5]\n"
     ]
    }
   ],
   "source": [
    "from typing import List\n",
    "\n",
    "class Solution:\n",
    "    def removeDuplicates(self, nums: List[int]) -> int:\n",
    "        if not nums:\n",
    "            return 0\n",
    "\n",
    "        # ポインターを初期化\n",
    "        write_index = 1\n",
    "\n",
    "        # numsを走査し、重複を削除\n",
    "        for i in range(1, len(nums)):\n",
    "            if nums[i] != nums[i - 1]:\n",
    "                nums[write_index] = nums[i]\n",
    "                write_index += 1\n",
    "\n",
    "        # 重複のない要素数を返す\n",
    "        return write_index\n",
    "\n",
    "# リストを定義する例\n",
    "nums = [1, 2, 2, 3, 4, 4, 5]\n",
    "\n",
    "solution = Solution()\n",
    "length = solution.removeDuplicates(nums)\n",
    "\n",
    "print(\"Length of unique elements:\", length)\n",
    "print(\"Modified list:\", nums[:length])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Length of unique elements: 5\n",
      "Modified list: [1, 2, 3, 4, 5, '_', '_']\n"
     ]
    }
   ],
   "source": [
    "from typing import List\n",
    "\n",
    "class Solution:\n",
    "    def removeDuplicates(self, nums: List[int]) -> int:\n",
    "        if not nums:\n",
    "            return 0\n",
    "\n",
    "        # ポインターを初期化\n",
    "        write_index = 1\n",
    "\n",
    "        # numsを走査し、重複を削除\n",
    "        for i in range(1, len(nums)):\n",
    "            if nums[i] != nums[i - 1]:\n",
    "                nums[write_index] = nums[i]\n",
    "                write_index += 1\n",
    "\n",
    "        # 残りの部分をNoneに設定\n",
    "        for i in range(write_index, len(nums)):\n",
    "            nums[i] = None\n",
    "\n",
    "        # 重複のない要素数を返す\n",
    "        return write_index\n",
    "\n",
    "# リストを定義する例\n",
    "nums = [1, 2, 2, 3, 4, 4, 5]\n",
    "\n",
    "solution = Solution()\n",
    "length = solution.removeDuplicates(nums)\n",
    "\n",
    "print(\"Length of unique elements:\", length)\n",
    "print(\"Modified list:\", nums)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
