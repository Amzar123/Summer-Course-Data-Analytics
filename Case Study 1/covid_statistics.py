import math

def calculate_statistics(nums):
    minimum = min(nums)
    maximum = max(nums)
    range_val = maximum - minimum
    mean = sum(nums) / len(nums)
    sorted_nums = sorted(nums)
    median = sorted_nums[math.floor(len(nums) / 2)]
    deviation = math.sqrt(sum([(num - mean) ** 2 for num in nums]) / len(nums))
    
    return minimum, maximum, range_val, mean, median, deviation

if __name__ == "__main__":
    nums = [174, 335, 278, 214, 422, 513, 737, 672, 489, 412, 1301, 1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342]

    min_val, max_val, range_val, mean_val, median_val, deviation_val = calculate_statistics(nums)

    print("Min: " + str(min_val))
    print("Max: " + str(max_val))
    print("Range: " + str(range_val))
    print("Mean: " + str(mean_val))
    print("Median: " + str(median_val))
    print("Standard Deviation: " + str(deviation_val))