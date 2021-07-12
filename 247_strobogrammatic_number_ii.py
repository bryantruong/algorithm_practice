class Solution:
    def findStrobogrammatic(self, n):
        """
        Function that returns all the strobogrammatic numbers of length n.
        It is given that 1 <= n <= 14.
        Recursive solution; The general approach is to populate the strobogrammatic numbers from the middle out.
        If n is even, start adding the pairings to the front and back around an empty string.
        If n is odd, start adding the pairings to the front and back around 0, 1, 8 (can't have 6 or 9 in the middle).
        There is a special case for if n == 2. We can't add the pairing for 0, since we don't allow leading zeros.
        :param num: desired length of the strings
        :return: list of strings
        """
        pairings = {'0': '0',
                    '1': '1',
                    '6': '9',
                    '8': '8',
                    '9': '6'}
        solution_list = []

        def recursive_build(center, characters_to_add):
            """
            Helper recursive function
            :param center: the existing string we are adding to
            :param characters_to_add: number of characters that we still need to add
            :return: N/A, just append the solution to the list
            """
            if characters_to_add == 0:
                solution_list.append(center)
                return
            for number in pairings:
                # It is a special case when characters_to_add is only 2, since we can't have the leading zeros
                if characters_to_add == 2 and number != '0':
                    # Add the number to the front, add its pairing to the back
                    # n-2, since we just added two more characters
                    recursive_build(number + center + pairings[number], characters_to_add - 2)
                # When characters_to_add is not 2 (greater than 2), we can put zeros in  (Ex: 1001 is valid)
                elif characters_to_add > 2:
                    recursive_build(number + center + pairings[number], characters_to_add - 2)
        if int(n) % 2 != 0:
            # If odd, we kick off the same process of adding to front and back, except we build around '0', '1', '8'
            # We subtract one, because once we manually add the center char, the process is the same as for evens
            for center_char in ['0', '1', '8']:
                recursive_build(center_char, n - 1)
        else:
            # If even, we can just start building the list from an empty string, since there is no middle char
            recursive_build("", int(n))
        return solution_list


if __name__ == '__main__':
    test_n = "2"
    solution_instance = Solution()
    print(solution_instance.findStrobogrammatic(test_n))
