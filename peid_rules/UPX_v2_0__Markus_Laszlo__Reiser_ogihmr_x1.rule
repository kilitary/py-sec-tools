rule _UPX_v2_0__Markus_Laszlo__Reiser_ogihmr
{
	meta:
		description = "UPX v2_0 __ Markus_ Laszlo _ Reiser"
	strings:
		$a = {55FF96????????09C07407890383C304EB??FF96????????8BAE????????8DBE00F0FFFFBB0010000050546A045357FFD58D87????000080207F8060287F585054505357FFD558618D4424806A0039C475FA83EC80}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
