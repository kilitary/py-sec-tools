rule _BopCrypt_v1_0_kdpugc
{
	meta:
		description = "BopCrypt v1_0"
	strings:
		$a = {60BD????????E8????0000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
