function code(str) {
    upper = toupper(str);

    if (index(upper, "POL") != 0)
        return "P";
    else if (index(upper, "HOA") != 0)
        return "H";
    else if (index(upper, "GOL") != 0)
        return "G";
    else if (index(upper, "BON") != 0)
        return "B";
    else if (index(upper, "UNDER") != 0)
        return "U";
    else if (index(upper, "OVER") != 0)
        return "O";
    else
        return "?";
}

BEGIN {
    FS="@";
    OFS="";
    ORS="\n";
}

{ print code($1), code($2), code($3), code($4), code($5); }

