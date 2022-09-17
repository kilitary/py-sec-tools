rule _CodeCrypt_v0_15b_jwchej
{
	meta:
		description = "CodeCrypt v0_15b"
	strings:
		$a = {E92E030000EB02833D58EB02FF1D5BEB020FC75FEB03FF1D34}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
