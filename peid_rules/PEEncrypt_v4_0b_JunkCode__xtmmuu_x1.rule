rule _PEEncrypt_v4_0b_JunkCode__xtmmuu
{
	meta:
		description = "PEEncrypt v4_0b _JunkCode_"
	strings:
		$a = {66????006683??00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
