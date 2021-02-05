rule _ENIGMA_Protector__Sukhov_Vladimir_hbrynx
{
	meta:
		description = "ENIGMA Protector __ Sukhov Vladimir"
	strings:
		$a = {456E69676D612070726F746563746F72207631}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
