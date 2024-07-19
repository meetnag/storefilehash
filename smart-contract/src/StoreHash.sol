pragma solidity 0.8.21;


contract StoreHash {

    address _contractOwner;

    event StoredHash(
        address indexed _sender,
        bytes32 _hash,
        uint256 _timeStored
    );

    error InvalidCaller(address _caller);

    constructor() {
        _contractOwner = msg.sender;
    }

    function storeHash(bytes32 _hash) public {

        if (msg.sender != _contractOwner)
            revert InvalidCaller(msg.sender);
        
        emit StoredHash(msg.sender, _hash, block.timestamp);

    }

}