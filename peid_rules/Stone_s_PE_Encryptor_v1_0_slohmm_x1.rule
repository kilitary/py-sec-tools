rule _Stone_s_PE_Encryptor_v1_0_slohmm
{
	meta:
		description = "Stone_s PE Encryptor v1_0"
	strings:
		$a = {606A006A206A026A006A0368000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
