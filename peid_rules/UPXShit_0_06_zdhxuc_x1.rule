rule _UPXShit_0_06_zdhxuc
{
	meta:
		description = "UPXShit 0_06"
	strings:
		$a = {B8????4300B915000000803408??E2FAE9D6FFFFFF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
