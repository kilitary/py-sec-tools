rule _ASDPack_2_0__asd_ujyjpv
{
	meta:
		description = "ASDPack 2_0 __ asd"
	strings:
		$a = {5B43837B74000F8408000000894314E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
