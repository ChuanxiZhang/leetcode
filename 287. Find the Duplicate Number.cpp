class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow= nums[0];
        int fast= nums[nums[0]];
        int slow2=0;
        if(nums.size()>1){
            while(slow!=fast){
                slow=nums[slow];
                fast=nums[nums[fast]];
            }
            while(slow!=slow2){
                slow=nums[slow];
                slow2=nums[slow2];
            }
            return slow;
        }
        return -1;
    }
};
