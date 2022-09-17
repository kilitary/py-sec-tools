rule _32Lite_v0_03a_omhloz
{
	meta:
		description = "32Lite v0_03a"
	strings:
		$a = {6006FC1E07BE????????6A0468??10????68}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
