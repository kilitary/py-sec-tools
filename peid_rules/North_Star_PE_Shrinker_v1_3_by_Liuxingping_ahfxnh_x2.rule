rule _North_Star_PE_Shrinker_v1_3_by_Liuxingping_ahfxnh
{
	meta:
		description = "North Star PE Shrinker v1_3 by Liuxingping"
	strings:
		$a = {9C60E8000000005DB8B38540002DAC8540002BE88DB573??FFFF8B0683F80074118DB57F??FFFF8B0683F8010F84F1010000C706010000008BD58B854F??FFFF2BD089954F??FFFF019567??FFFF8DB583??FFFF01}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
