rule _CodeCrypt_v0_15b_ioxilo
{
	meta:
		description = "CodeCrypt v0_15b"
	strings:
		$a = {E931030000EB02833D58EB02FF1D5BEB020FC75F}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
