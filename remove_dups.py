def removeDuplicates(nums):
  """
  :type nums: List[int]
  :rtype: int
  """
  filler_char = '_'
  
  # Replace duplicate chars with filler underscore
  for i in range(len(nums) - 1):
    if nums[i] == nums[i + 1]:
      nums[i] = filler_char
  
  # Remove filler underscores from list
  try:
    while True:
      nums.remove(filler_char)
  except ValueError:
    pass
  
  return len(nums), nums

print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
