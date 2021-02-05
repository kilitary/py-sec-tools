rule _Hasp_4_envelope_dongle_Alladin__pzvkql
{
	meta:
		description = "Hasp 4 envelope dongle _Alladin_"
	strings:
		$a = {1002D0510F0083}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
