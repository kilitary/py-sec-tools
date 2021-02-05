rule _CodeCrypt_v0_164_hmhpge
{
	meta:
		description = "CodeCrypt v0_164"
	strings:
		$a = {E92E030000EB02833D58EB02FF1D5BEB020FC75F}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
