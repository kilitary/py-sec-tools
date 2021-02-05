rule _eXPressor_V1_0__CGSoftLabs_hzphde
{
	meta:
		description = "eXPressor V1_0 __ CGSoftLabs"
	strings:
		$a = {E935140000E931130000E998120000E9EF0C0000E942130000E9E9020000E9EF0B0000E91B0D0000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
