"""
1 2 3 4 5 6 7

price

2 4 6 1 7 3 5

choose 3 consecutive index object that combine up to make a larget price

Group 2 = group - first element of grounp1 + last element of group 2(newly added)
"""

def best_choclates(prices, window_size):
    current_total = sum(prices[0:window_size])
    best_total = current_total

    print(f"Window !: {prices[0:window_size]} = {current_total}")

    for i in range(window_size, len(prices)):
        left_chocolate = prices[i - window_size]
        right_choclate = prices[i]

        current_total = current_total - left_chocolate + right_choclate

        window = prices[i - window_size + 1 : i+1]
        print(f"Window : {window} = {current_total}")

        if current_total > best_total:
            best_total = current_total
    
    return best_total

prices = [2, 4, 6, 1, 7, 3, 5, 3]
answer = best_choclates(prices, 3)
print("best total is ", answer)


#leetcode maximum-number-of-vowels-in-a-substring-of-given-length 1456


def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Count vowels in the first window of size k
        current_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
                
        max_vowels = current_vowels
        
        # Slide the window across the string
        for i in range(k, len(s)):
            # Remove the character leaving the window
            if s[i - k] in vowels:
                current_vowels -= 1
            # Add the character entering the window
            if s[i] in vowels:
                current_vowels += 1
                
            # Update the maximum count found so far
            if current_vowels > max_vowels:
                max_vowels = current_vowels
                
        return max_vowels

#Leetcode: grumpy-bookstore-owner 1052


def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        n = len(customers)
        
        # 1. Calculate baseline satisfied customers (when owner is already not grumpy)
        baseline_satisfied = sum(customers[i] for i in range(n) if grumpy[i] == 0)
        
        # 2. Use a sliding window to find the max extra customers we can satisfy
        # First, calculate the extra gain for the very first window of size `minutes`
        current_window_gain = sum(customers[i] for i in range(minutes) if grumpy[i] == 1)
        max_window_gain = current_window_gain
        
        # Slide the window across the remaining minutes
        for i in range(minutes, n):
            # Add the new element entering the window if the owner was grumpy
            if grumpy[i] == 1:
                current_window_gain += customers[i]
            
            # Remove the element leaving the window if the owner was grumpy
            if grumpy[i - minutes] == 1:
                current_window_gain -= customers[i - minutes]
                
            # Keep track of the maximum gain seen so far
            max_window_gain = max(max_window_gain, current_window_gain)
            
        # 3. Maximum total satisfied is baseline + the best possible gain
        return baseline_satisfied + max_window_gain


