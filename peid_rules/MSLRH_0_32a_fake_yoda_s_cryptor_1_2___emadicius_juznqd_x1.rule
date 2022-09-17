rule _MSLRH_0_32a_fake_yoda_s_cryptor_1_2___emadicius_juznqd
{
	meta:
		description = "MSLRH 0_32a _fake yoda_s cryptor 1_2_ __ emadicius"
	strings:
		$a = {53558BE833DBEB600D0A0D0A57575061636B3332206465636F6D7072657373696F6E20726F7574696E652076657273696F6E20312E31320D0A28632920313939382050696F747220576172657A616B20616E642052}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
