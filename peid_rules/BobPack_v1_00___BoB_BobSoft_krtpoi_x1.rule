rule _BobPack_v1_00___BoB_BobSoft_krtpoi
{
	meta:
		description = "BobPack v1_00 ___ BoB  BobSoft"
	strings:
		$a = {60E8000000008B0C2489CD83E90681ED????????E83D0000008985????????89C2B85D0A00008D0408E8E40000008B700401D6E876000000E851010000E80101}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
