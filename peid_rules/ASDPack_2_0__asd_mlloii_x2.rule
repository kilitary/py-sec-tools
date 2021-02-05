rule _ASDPack_2_0__asd_mlloii
{
	meta:
		description = "ASDPack 2_0 __ asd"
	strings:
		$a = {8B442404565753E8CD010000C30000000000000000000000000010000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
