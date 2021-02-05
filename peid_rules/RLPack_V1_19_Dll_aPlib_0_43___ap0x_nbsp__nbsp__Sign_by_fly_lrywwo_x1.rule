rule _RLPack_V1_19_Dll_aPlib_0_43___ap0x_nbsp__nbsp__Sign_by_fly_lrywwo
{
	meta:
		description = "RLPack V1_19 Dll _aPlib 0_43_ __ ap0x_nbsp_ _nbsp__ Sign by fly"
	strings:
		$a = {807C2408010F858901000060E8000000008B2C2483C404837C242801750C8B44242489853C040000EB0C8B853804000089853C0400008DB5600400008D9DEB02000033FFE852010000EB1B8B853C040000FF743704}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
