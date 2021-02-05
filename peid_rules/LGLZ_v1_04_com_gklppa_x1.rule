rule _LGLZ_v1_04_com_gklppa
{
	meta:
		description = "LGLZ v1_04 _com"
	strings:
		$a = {BF????3BFC7219B409BA1201CD21B44CCD21}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
