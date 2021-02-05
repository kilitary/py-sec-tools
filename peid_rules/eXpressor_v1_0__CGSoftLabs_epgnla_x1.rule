rule _eXpressor_v1_0__CGSoftLabs_epgnla
{
	meta:
		description = "eXpressor v1_0 __ CGSoftLabs"
	strings:
		$a = {E935140000E931130000E998120000E9EF0C0000E94213}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
