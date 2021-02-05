rule _DOS_Device_Driver_rtghkz
{
	meta:
		description = "DOS Device Driver"
	strings:
		$a = {FFFFFFFF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
