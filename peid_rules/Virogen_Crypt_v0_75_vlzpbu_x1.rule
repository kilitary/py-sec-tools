rule _Virogen_Crypt_v0_75_vlzpbu
{
	meta:
		description = "Virogen Crypt v0_75"
	strings:
		$a = {9C55E8EC00000087D55D6087D580BD1527400001}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
