// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./Vault2.sol";

contract VaultFactory {

    event InstanceCreated(address instanceAddress);
    address private owner;

    constructor() {
        owner = msg.sender;
    }
    function createInstance(address player) public payable returns(address){
        require(msg.sender == owner); // sanity check, if player gets a hold of ABI
        Vault2 instance = new Vault2(player);
        emit InstanceCreated(address(instance));
        return address(instance);
    }

    function validateInstance(address payable _instance, address _player) public view returns (bool) {
        Vault2 instance = Vault2(_instance);
        return instance.owner() == _player;
    }
}