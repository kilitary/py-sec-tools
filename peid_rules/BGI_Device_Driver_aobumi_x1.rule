rule _BGI_Device_Driver_aobumi
{
	meta:
		description = "BGI Device Driver"
	strings:
		$a = {706B080842474920}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
