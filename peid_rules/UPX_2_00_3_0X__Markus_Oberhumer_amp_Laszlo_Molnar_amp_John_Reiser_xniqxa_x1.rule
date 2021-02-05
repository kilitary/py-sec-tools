rule _UPX_2_00_3_0X__Markus_Oberhumer_amp_Laszlo_Molnar_amp_John_Reiser_xniqxa
{
	meta:
		description = "UPX 2_00_3_0X __ Markus Oberhumer _amp_ Laszlo Molnar _amp_ John Reiser"
	strings:
		$a = {5E89F7B9????????8A07472CE83C0177F7803F??75F28B078A5F0466C1E808C1C01086C429F880EBE801F0890783C70588D8E2D98D??????????8B0709C0743C8B5F048D????????????01F35083C708FF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
