// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Test} from "forge-std/Test.sol";
import {StoreHash} from "../src/StoreHash.sol";

contract StoreHashTest is Test {

    /// @dev    event to emit
    event StoredHash(
        address indexed _sender,
        bytes32 _hash,
        uint256 _timeStored
    );

    StoreHash public storeHashContract;

    /// @dev    setup
    function setUp() public {
        storeHashContract = new StoreHash();
    }

    /// @dev    Test event data
    function testFuzz_Event(bytes32 _hash) public {
        
        vm.expectEmit(
            true, 
            false, 
            false, 
            false
        );

        emit StoredHash(
            address(this),
            _hash, 
            block.timestamp
        );

        storeHashContract.storeHash(_hash); 

    }

    /// @dev    Test revert
    function testFuzz_CallerRevert(bytes32 _hash) public {

        address _invalidCaller = vm.addr(10);

        /// @dev    revert expected
        vm.expectRevert(
            abi.encodeWithSelector(
                StoreHash.InvalidCaller.selector, 
                _invalidCaller
            )
        );

        /// @dev    expected caller to be reverted
        vm.prank(_invalidCaller);
        storeHashContract.storeHash(_hash); 

    }
}
