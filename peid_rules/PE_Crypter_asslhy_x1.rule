rule _PE_Crypter_asslhy
{
	meta:
		description = "PE_Crypter"
	strings:
		$a = {60E8000000005DEB26}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
