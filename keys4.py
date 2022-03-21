data = 'hghfy/vw1XIyvAo0uDK5I81N1ZsA5gCF1exFH8xNECN1kyr4Fjj4iVnGkxLgLo8+JZ1PUmHkZSMghF8eeQ8RDpRhb/p+NMpupjRypZKVy+5iCmQerjPL4Nzb+SipGQwgPsSWC0KwPAPKrAvnZvDxhfekNA30R/k8Bk+H1UX8jW4='
nums = ''
for i in data:
    nums += str(ord(i)) + '|'

print(nums[:-1])

simb_nums = nums.split('|')
simbs = ''
for i in simb_nums:
    try:
        simbs += chr(int(i))
    except Exception as e:
        break

print(simbs)