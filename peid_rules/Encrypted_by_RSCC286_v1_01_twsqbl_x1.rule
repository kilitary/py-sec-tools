rule _Encrypted_by_RSCC286_v1_01_twsqbl
{
	meta:
		description = "Encrypted by_ RSCC286 v1_01"
	strings:
		$a = {FE525343432F312E3031FE}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
