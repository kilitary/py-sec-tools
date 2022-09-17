rule _NsPack_V1_3__LiuXingPing_phlken
{
	meta:
		description = "NsPack V1_3 __ LiuXingPing"
	strings:
		$a = {9C60E8000000005DB8B38540002DAC854000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
