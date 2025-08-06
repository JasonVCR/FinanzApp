@echo off
echo ====================================
echo   SISTEMA DE COLORES DE COMPATIBILIDAD
echo ====================================
echo.
echo Este menu te permite probar el sistema de colores implementado
echo.
echo 1. Prueba basica de colores
echo 2. Demostracion completa de rangos
echo 3. Prueba con calculo mejorado
echo 4. Demostracion perfecta (todos los rangos)
echo 5. Ejecutar sistema completo de automatizacion
echo 6. Salir
echo.
set /p choice=Selecciona una opcion (1-6): 

if "%choice%"=="1" (
    echo.
    echo Ejecutando prueba basica de colores...
    python test_compatibility_colors.py
    pause
    goto menu
)

if "%choice%"=="2" (
    echo.
    echo Ejecutando demostracion completa de rangos...
    python demo_compatibility_colors.py
    pause
    goto menu
)

if "%choice%"=="3" (
    echo.
    echo Ejecutando prueba con calculo mejorado...
    python improved_compatibility_test.py
    pause
    goto menu
)

if "%choice%"=="4" (
    echo.
    echo Ejecutando demostracion perfecta (todos los rangos)...
    python perfect_color_demo.py
    pause
    goto menu
)

if "%choice%"=="5" (
    echo.
    echo Ejecutando sistema completo de automatizacion...
    python simple_automation.py
    pause
    goto menu
)

if "%choice%"=="6" (
    echo.
    echo Saliendo...
    exit
)

echo Opcion invalida. Por favor selecciona 1-6.
pause

:menu
cls
goto :eof
