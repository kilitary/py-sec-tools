rule _nPack_v1_1_300_2006_Beta_vkokwz
{
	meta:
		description = "nPack v1_1_300_2006 Beta"
	strings:
		$a = {833D4C????00007505E901000000C3E846000000E873000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
