pragma solidity ^0.4.21;

contract CaptureTheEther {
    
    struct Student {
        mapping (int => bool) solved;
        int score;
    }

    // studentID: lowercase and number. ex: b02902055
    mapping (string => Student) students;

    // challenge 0: call me, 10 points
    function callMe(string studentID) public {
        int challengeID = 0;
        int point = 10;
        require(students[studentID].solved[challengeID] != true);

        students[studentID].solved[challengeID] = true;
        students[studentID].score += point;
    }

    // challenge 1: guess the number, 10 points
    int c1Ans = 777;
    function guessTheNumber(string studentID, int numberGuessed) public {
        int challengeID = 1;
        int point = 10;
        require(students[studentID].solved[challengeID] != true);

        if (numberGuessed != c1Ans) {
            return;
        }
        students[studentID].solved[challengeID] = true;
        students[studentID].score += point;
    }

    // challenge 2: bribe me, 20 points
    function bribeMe(string studentID) public payable {
        int challengeID = 2;
        int point = 20;
        require(students[studentID].solved[challengeID] != true);
        require(msg.value == 1 ether);
        students[studentID].solved[challengeID] = true;
        students[studentID].score += point;
    }

    // challenge 3: guess secret number, 50 points
    function guessSecretNumber(string studentID, uint8 numberGuessed) public {
        int challengeID = 3;
        int point = 50;
        require(students[studentID].solved[challengeID] != true);
        
        bytes32 answerHash = 0x313b2ea16b36f2e78c1275bfcca4e31f1e51c3a5d60beeefe6f4ec441e6f1dfc;
        if (keccak256(numberGuessed) != answerHash) {
            return;
        }
        students[studentID].solved[challengeID] = true;
        students[studentID].score += point;
    }

    // challenge 4: guess random number, 70 points
    uint16 c4Ans;
    function guessRandomNumber(string studentID, uint16 numberGuessed) public {
        int challengeID = 4;
        int point = 70;
        require(students[studentID].solved[challengeID] != true);
        
        if (numberGuessed != c4Ans) {
            return;
        }
        students[studentID].solved[challengeID] = true;
        students[studentID].score += point;
    }

    // challenge 5: guess runtime random number, 90 points
    function guessRuntimeRandomNumber(string studentID, uint16 numberGuessed) public {
        int challengeID = 5;
        int point = 90;
        require(students[studentID].solved[challengeID] != true);
        
        uint16 c5Ans = uint16(keccak256(blockhash(block.number - 1), block.timestamp));
        if (numberGuessed != c5Ans) {
            return;
        }
        students[studentID].solved[challengeID] = true;
        students[studentID].score += point;
    }

    function getScore(string studentID) view public returns (int) {
        return students[studentID].score;
    }
    
    function getSolvedStatus(string studentID, int challengeID) view public returns (bool) {
        return students[studentID].solved[challengeID];
    }

    constructor() public {
        c4Ans = uint16(keccak256(blockhash(block.number - 1), block.timestamp));
    }
}