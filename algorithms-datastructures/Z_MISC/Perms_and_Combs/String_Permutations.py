"""
@author: David Lei
@since: 22/08/2016
@modified: 

Java coe
package Algo_Ds_Practice.Permutations;

/**
 * Created by David on 14/04/2016.
 * Time: 2:04 AM
 */

public class Permutations {


    public static void main(String[] args) {

        permuteStart("12");

    }

    public static void permuteStart ( String str ) {
        permute( str.toCharArray(), 0, str.length()-1 ); }

    public static void permute( char [] str, int low, int high ) {
        if ( low == high ) {
            String a = new String(str);
            System.out.println(a);
        }
        else {
            char tmp = str[ low ];
            for ( int i = low; i <= high; i++ ) {
                str[ low ] = str[ i ];
                str[ i ] = tmp;
                permute( str, low+1, high );
                str[ i ] = str[ low ];
            }
            str[ low ] = tmp; }
    }
}

"""
"""
@author: David Lei
@since: 14/06/2016
@modified:

Final all permutations of a string of the length of the string
"""

def permutations(input_string):
    if len(input_string) <= 1:      # base case, string of length 1
        return input_string
    else:
        removed_first_char = input_string[1:]
        len_minus_one_perms = permutations(removed_first_char)  # permutations of len - 1
        removed_character = input_string[0]
        results = []
        for a_permutation in len_minus_one_perms:               # for each permutation of len - 1
            for i in range(len(len_minus_one_perms) + 1):       # insert removed char at every location
                concatenated = a_permutation[:i] + removed_character + a_permutation[i:]
                results.append(concatenated)
        return results
count_call = 0
count_modify_current_perm = 0
count_for_p_in_perms = 0
def permutations_2(string):
    global count_call
    count_call += 1
    print("Count called: " + str(count_call))
    if len(string)<=1:
        return string
    perms = permutations_2(string[1:])
    char = string[0]
    result = []
    for perm in perms:
        global count_for_p_in_perms
        count_for_p_in_perms += 1
        print("For p in perms count: " + str(count_for_p_in_perms))
        for i in range(len(perm)+1):
            global count_modify_current_perm
            count_modify_current_perm+= 1
            print("Modify current perm count: " + str(count_modify_current_perm))
            result.append(perm[:i] + char + perm[i:])
    return result



#https://www.youtube.com/watch?v=nYFd7VHKyWQ&list=PLrmLmBdmIlpslxZUHHWmfOzNn6cA7jvyh

if __name__ == "__main__":
    s = 'aaaaaaaaaaa'
    p = permutations_2(s)
    print("Permutations of a string of length: " + str(len(s)) + "\nNumber of permutations")
    print(len(p))
    print(p)


    print(permutations("abc"))