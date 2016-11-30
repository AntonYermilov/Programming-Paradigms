#!/usr/bin/env ruby

def copy(a, b, l, r)
  while l < r
    b[l] = a[l]
    l += 1
  end
end

def get_number_of_inversions(a, b, left, right)
  number_of_inversions = 0
  return 0 if right - left <= 1

  mid = left + (right - left) / 2
  number_of_inversions += get_number_of_inversions(a, b, left, mid)
  number_of_inversions += get_number_of_inversions(a, b, mid, right)

  copy(a, b, left, mid)
  i, j, k = left, mid, left
  while i < mid and j < right
    if a[j] < b[i]
      a[k] = a[j]
      j += 1
      number_of_inversions += mid - i
    else
      a[k] = b[i]
      i += 1
    end
    k += 1
  end
  while i < mid
    a[k] = b[i]
    k += 1
    i += 1
  end
  return number_of_inversions
end

# def brute_force(a)
#   n = a.size - 1
#   return 0 if n == 0
#   a[0..n - 1].map.with_index { |item, idx| a[idx + 1..n].count { |i| i < item } }.inject(:+)
# end

if __FILE__ == $0
  # n, *a = STDIN.read.split().map(&:to_i)
  # b = Array.new(n, 0)
  # puts "#{get_number_of_inversions(a, b, 0, n)}"
  # 1000.times do |_|
  n = rand(1..10000)
  a = Array.new(n) { rand(1..1000000) }
  b = Array.new(n, 0)
  answer = get_number_of_inversions(a, b, 0, n)
  puts answer
  # end
end
