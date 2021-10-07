# Change Variable Values
x = int(input('Enter  X Value: '))
y = int(input('Enter Y Value: '))
print(f'This is after the swap: {x} and {y}')

x = x + y
y = x - y
x = x - y

print(f'This is after the swap: {x} and {y}')

# TCP 3 way handshake is basically a process for the client to connect to the server to create a reliable connection.to do this the client first sends a SYN (Synchronize Sequence Number)
# to the server and
# then the server sends a SYN + ACK to the client and then the Client sends the Acknowledgement to the server to create a reliable connection between them
# that then allows the client and server to have a safe and secure data transfer

# Reverse Linked List
head = [1, 2, 3, 4, 5, 6]


def item(self, head):
    previous, current = None, head

    while current:
        nxt = current.next
        current.next = previous
        previous = current
        current = nxt
    return previous


# Palindrome linked list
def Palindrome(self, head):
    nums = []

    while head:
        nums.append(head.val)
        head = head.next

    l, r = 0, len(nums) - 1
    while l <= r:
        if nums[l] != nums[r]:
            return False
        l += r
        r -= l
    return True

    # Palindrome in O(n) time and O(1) [constant] space!
    fast = head
    slow = head
    # Find middle (slow)
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # Reverse second half
    prev = None
    while slow:
        tmp = slow.next
        sslow.next = prev
        prev = slow
        slow = tmp

    # check palindrome
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True


# Fibonacci
# Recursion
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


nterms = int(input("Enter the terms: "))  # take input from the user

if nterms <= 0:  # check if the number is valid
    print("Please enter a positive integer ")
else:
    print("Fibonacci sequence: ")
    for i in range(nterms):
        print(fib(i))

# Loop Fibonacci
# Enter number of terms needed                   #0,1,1,2,3,5....
a = int(input("Enter the terms: "))
first = 0                                         # first element of series
second = 1                                         # second element of series
if a <= 0:
    print("The requested series is", first)
else:
    print(first, second, end=" ")
    for x in range(2, a):
        Next = first + second
        print(Next, end=" ")
        first = second
        second = Next
#