rule _ENIGMA_Protector_V1_0_V1_2__Sukhov_Vladimir_vyvetk
{
	meta:
		description = "ENIGMA Protector V1_0_V1_2__ Sukhov Vladimir"
	strings:
		$a = {60E8000000005D83????81}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
