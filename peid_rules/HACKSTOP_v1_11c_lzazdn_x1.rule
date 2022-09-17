rule _HACKSTOP_v1_11c_lzazdn
{
	meta:
		description = "HACKSTOP v1_11c"
	strings:
		$a = {B430CD2186E03D????73??B4??CD21B0??B44CCD2153BB????5BEB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
