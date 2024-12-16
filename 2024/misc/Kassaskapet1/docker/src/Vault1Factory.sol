// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./Vault1.sol";

contract VaultFactory {

    event InstanceCreated(address instanceAddress);
    address private owner;

    constructor() {
        owner = msg.sender;
    }
    function createInstance() public payable returns(address){
        require(msg.sender == owner); // sanity check, if player gets ahold of abi
        Vault instance = new Vault("PrivateNotPrivate");
        emit InstanceCreated(address(instance));
        return address(instance);
    }

    function validateInstance(address payable _instance, address _player) public view returns (bool) {
        Vault instance = Vault(_instance);
        return instance.owner() == _player;
    }
}